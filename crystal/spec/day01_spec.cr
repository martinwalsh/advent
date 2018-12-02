require "spec"
require "../src/day01.cr"

describe "Day01" do
  context "with part1 examples" do
    it "should correctly adjust frequencies" do
      Day01.part1(["+1", "+1", "+1"]).should eq(3)
      Day01.part1(["+1", "+1", "-2"]).should eq(0)
      Day01.part1(["-1", "-2", "-3"]).should eq(-6)
    end
  end

  context "with part2 examples" do
    it "should correctly calibrate" do
      Day01.part2(["+1", "-1"]).should eq(0)
      Day01.part2(["+3", "+3", "+4", "-2", "-4"]).should eq(10)
      Day01.part2(["-6", "+3", "+8", "+5", "-6"]).should eq(5)
      Day01.part2(["+7", "+7", "-2", "-7", "-4"]).should eq(14)
    end
  end

  context "with real input for part1" do
    it "should correctly adjust frequencies" do
      Day01.part1(File.read("/data/day01-marty.txt").lines).should eq(582)
    end
  end

  context "with real input for part2" do
    it "should correctly calibrate" do
      Day01.part2(File.read("/data/day01-marty.txt").lines).should eq(488)
    end
  end
end
