require "spec"
require "../src/dayNN.cr"

describe "DayNN" do
  context "check part1" do
    it "is nil" do
      DayNN.part1.should be_nil
    end
  end

  context "check part2" do
    it "is nil" do
      DayNN.part2.should be_nil
    end
  end

  context "in the data directory" do
    it "can read a file" do
      File.read("/data/dayNN.txt").should eq("")
    end
  end
end

