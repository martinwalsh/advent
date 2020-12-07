defmodule Advent.Input.StringData do
  defmacro __using__(opts) do
    quote bind_quoted: [opts: opts] do
      import Advent.Input.StringData

      @delimiter Keyword.fetch!(opts, :delimiter)

      alias Advent.Input.Data

      use Data
      @behaviour Data

      @impl Data
      def data do
        File.read!(path())
        |> String.trim()
        |> String.split(@delimiter)
      end
    end
  end
end
