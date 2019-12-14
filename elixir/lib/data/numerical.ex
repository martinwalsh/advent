defmodule Data.Numerical do
  defmacro __using__(_) do
    quote do
      defp path do
        "/data/" <> (Module.split(__MODULE__) |> List.last() |> String.downcase()) <> "-2019.txt"
      end

      defp data do
        File.read!(path())
        |> String.split("\n")
        |> Enum.drop(-1)
        |> Enum.map(&String.to_integer/1)
      end

      defp sum(numbers) do
        Enum.reduce(numbers, 0, fn n, acc -> n + acc end)
      end
    end
  end
end
