module Day01
  extend self

  def calibrate(seq, freq=0, &block)
    seq.each do |item|
      operator, value = item.chars.first, item[1..-1].to_i

      # I think I'd like to do something like freq.send(operator, value)
      # but Crystal lacks Ruby's reflection (stuff like eval and send).

      if operator == '+'
        freq += value
      elsif operator == '-'
        freq -= value
      else
        raise Exception.new("Invalid input item: #{item}")
      end

      yield freq
    end
  end

  def calibrate(seq, freq=0)
    freqs = [] of Int32
    calibrate(seq, freq) do |item|
      freqs.push item
    end
    freqs
  end

  def part1(seq)
    calibrate(seq).last
  end

  def part2(seq, freq=0)
    seen = Set.new [freq]
    1000.times do
      calibrate(seq, freq) do |fq|
        return fq if seen.includes?(fq)
        seen.add(fq)
        freq = fq
      end
    end
  end
end
