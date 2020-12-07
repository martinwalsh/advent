defmodule Advent.Input.Data do
  @callback data() :: [term]

  defmacro __using__(_) do
    quote do
      import Advent.Input.Data

      defp year do
        Application.get_env(:advent, :year)
      end

      defp path do
        day =
          Module.split(__MODULE__)
          |> List.last()
          |> String.downcase()

        year = System.get_env("YEAR", "2020")
        "/data/#{day}-#{year}.txt"
      end
    end
  end
end
