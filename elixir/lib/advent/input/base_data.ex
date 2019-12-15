defmodule Advent.Input.BaseData do
  defmacro __using__(_) do
    quote do
      defp path do
        "/data/" <> (Module.split(__MODULE__) |> List.last() |> String.downcase()) <> "-2019.txt"
      end

      defp data do
        File.read!(path())
        |> String.split("\n")
        |> Enum.drop(-1)
      end

      defoverridable data: 0
    end
  end
end
