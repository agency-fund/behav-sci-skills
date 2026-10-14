-- api/schema.sql: the site's tables in Supabase (Postgres).
--
-- Run once in the Supabase dashboard: SQL Editor -> New query -> paste -> Run.
-- Safe to run again; it only creates what is missing.
--
-- Only the site's server functions (api/*.py) touch these tables, using the
-- secret key, which bypasses Row Level Security. RLS is on with no policies and
-- the public roles have no grants, so the publishable (anon) key can read or
-- write nothing. The besci_ prefix keeps these apart from anything else in the
-- project.

create table if not exists besci_users (
  id          bigint generated always as identity primary key,
  google_sub  text not null unique,          -- Google's stable account id
  email       text not null,
  name        text,
  domain      text,
  org         text,                          -- TAF, IL, Guest, or empty
  can_review  boolean not null default false, -- as of the last sign-in; the server rechecks every request
  is_admin    boolean not null default false, -- may hide and delete ratings (ADMIN_EMAILS also grants this)
  first_seen  timestamptz not null default now(),
  last_seen   timestamptz not null default now(),
  sign_ins    integer not null default 1
);

create table if not exists besci_expert_reviews (
  id            bigint generated always as identity primary key,
  user_id       bigint not null references besci_users (id),
  skill         text not null,
  skill_version text not null,
  verdict       text not null,
  issue_number  integer not null,            -- the GitHub issue holding the review itself
  created_at    timestamptz not null default now()
);
create index if not exists besci_expert_reviews_user_time on besci_expert_reviews (user_id, created_at);

create table if not exists besci_ratings (
  id            bigint generated always as identity primary key,
  user_id       bigint not null references besci_users (id),
  skill         text not null,
  skill_version text not null,               -- the version that was rated
  stars         smallint not null check (stars between 1 and 5),
  comment       text check (char_length(comment) <= 2000),
  anonymous     boolean not null default false,
  display_name  text,                        -- shown unless anonymous
  org           text,                        -- TAF or IL shows a staff badge unless anonymous
  hidden        boolean not null default false, -- a maintainer hid the comment
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  unique (skill, user_id)                    -- one rating per person per skill; rating again updates it
);
create index if not exists besci_ratings_skill on besci_ratings (skill);
alter table besci_ratings add column if not exists org text;  -- for databases set up before the column existed

create table if not exists besci_events (    -- server-side analytics: sign_in, review_denied_domain, review_filed, rating_saved
  id         bigint generated always as identity primary key,
  user_id    bigint references besci_users (id),
  name       text not null,
  skill      text,
  props      jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);
create index if not exists besci_events_name_time on besci_events (name, created_at);

alter table besci_users          enable row level security;
alter table besci_expert_reviews enable row level security;
alter table besci_ratings        enable row level security;
alter table besci_events         enable row level security;

revoke all on besci_users, besci_expert_reviews, besci_ratings, besci_events from anon, authenticated;
