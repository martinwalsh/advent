defmodule Advent.Input.DirectionalData do
  @callback collect(String.t()) :: [term]

  defmacro __using__(_opts) do
    quote do
      alias Advent.Input.Data

      use Data
      @behaviour Data

      @impl Data
      def data do
        File.read!(path())
        |> String.split("\n")
        |> Enum.drop(-1)
        |> Enum.map(&collect/1)
      end
    end
  end
end
