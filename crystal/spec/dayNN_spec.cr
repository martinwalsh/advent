require "spec"
require "../src/dayNN.cr"

describe "DayNN" do
  example1 = <<-EOF
  EOF

  data = uninitialized String
  before_all do
    data = File.read("/data/dayNN.txt")
  end

  context "check examples" do
    it "is valid" do
      DayNN.part1(example1).should be_nil
      DayNN.part2(example1).should be_nil
    end
  end

  context "check part1" do
    it "is valid" do
      DayNN.part1(data).should be_nil
    end
  end

  context "check part2" do
    it "is valid" do
      DayNN.part2(data).should be_nil
    end
  end
end