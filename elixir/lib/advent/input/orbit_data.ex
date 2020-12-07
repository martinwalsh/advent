defmodule Advent.Input.OrbitData do
  defmacro __using__(_) do
    quote do
      import Advent.Input.OrbitData

      use Advent.Input.Data
      @behaviour Advent.Input.Data

      @impl Advent.Input.Data
      def data do
        File.read!(path())
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")"))
        |> Enum.map(&List.to_tuple/1)
      end
    end
  end
end
