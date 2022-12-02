require "spec"
require "../src/day01.cr"

describe "Day01" do
  example1 = <<-EOF
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
  EOF

  data = uninitialized String
  before_all do
    data = File.read("/data/day01.txt")
  end

  context "check examples" do
    it "is correct" do
      Day01.part1(example1).should eq(24000)
      Day01.part2(example1).should eq(45000)
    end
  end

  context "check part1" do
    it "is correct" do
      Day01.part1(data).should eq(68775)
    end
  end

  context "check part2" do
    it "is correct" do
      Day01.part2(data).should eq(202585)
    end
  end
end
