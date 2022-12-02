module Day01
  extend self

  def parse(data : String)
    return data.strip().split("\n\n").map(){ |e|
      e.split("\n").map(){ |s| s.to_i }.sum()
    }
  end

  def part1(data : String)
    return parse(data).max()
  end

  def part2(data : String)
    return parse(data).sort_by { |i| -i }.first(3).sum()
  end
end
