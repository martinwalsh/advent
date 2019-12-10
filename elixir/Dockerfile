FROM elixir:1.9.4

ENV MIX_ENV dev
WORKDIR /app

COPY mix.exs /app/

RUN mix local.hex --force && \
      mix local.rebar --force && \
      mix do deps.get, deps.compile
