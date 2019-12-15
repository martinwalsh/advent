defmodule Advent.Input.IntegerData do
  defmacro __using__(opts) do
    quote bind_quoted: [opts: opts] do
      import Advent.Input.IntegerData

      @delimiter Keyword.fetch!(opts, :delimiter)

      alias Advent.Input.Data

      use Data
      @behaviour Data

      @impl Data
      def data do
        File.read!(path())
        |> String.split(@delimiter)
        |> Enum.drop(-1)
        |> Enum.map(&String.to_integer/1)
      end
    end
  end

  def sum(numbers) do
    Enum.reduce(numbers, 0, fn n, acc -> n + acc end)
  end
end
