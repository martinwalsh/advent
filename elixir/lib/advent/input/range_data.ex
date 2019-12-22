defmodule Advent.Input.RangeData do
  defmacro __using__(opts) do
    quote bind_quoted: [opts: opts] do
      import Advent.Input.RangeData

      alias Advent.Input.Data

      use Data
      @behaviour Data

      @impl Data
      def data do
        [first, last] =
          File.read!(path())
          |> String.trim()
          |> String.split("-")
          |> Enum.map(&String.to_integer/1)

        {first, last, Range.new(first, last) |> Enum.map(&Integer.to_string/1)}
      end
    end
  end
end
