defmodule Advent.Input.IntegerData do
  defmacro __using__(opts) do
    quote bind_quoted: [opts: opts] do
      use Advent.Input.BaseData

      @delimiter Keyword.fetch!(opts, :delimiter)

      defp data do
        File.read!(path())
        |> String.split(@delimiter)
        |> Enum.drop(-1)
        |> Enum.map(&String.to_integer/1)
      end

      defp sum(numbers) do
        Enum.reduce(numbers, 0, fn n, acc -> n + acc end)
      end
    end
  end
end
