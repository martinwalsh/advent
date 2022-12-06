import * as fs from "fs";
import { part1, part2 } from "./dayNN";

var data = fs.readFileSync("/data/dayNN.txt", "utf-8");
var EXAMPLE1 = `
`;

describe("check examples", () => {
    it("is correct", () => {
        expect(part1(EXAMPLE1)).toEqual(undefined);
        expect(part2(EXAMPLE1)).toEqual(undefined);
    });
});

describe("check part1", () => {
    it("is correct", () => {
        expect(part1(data)).toEqual(undefined);
    });
});

describe("check part2", () => {
    it("is correct", () => {
        expect(part2(data)).toEqual(undefined);
    });
});
