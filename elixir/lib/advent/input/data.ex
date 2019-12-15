defmodule Advent.Input.Data do
  @callback data() :: [term]

  defmacro __using__(_) do
    quote do
      import Advent.Input.Data

      defp path do
        day =
          Module.split(__MODULE__)
          |> List.last()
          |> String.downcase()

        "/data/#{day}-2019.txt"
      end
    end
  end
end
