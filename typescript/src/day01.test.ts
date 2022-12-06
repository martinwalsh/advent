import * as fs from "fs"
import { part1, part2 } from "./day01"

var data = fs.readFileSync("/data/day01.txt", "utf-8")
var EXAMPLE1 = `
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
`

describe("check examples", () => {
    it("is correct", () => {
        expect(part1(EXAMPLE1)).toEqual(24000);
        expect(part2(EXAMPLE1)).toEqual(45000);
    });
});

describe("check part1", () => {
    it("is correct", () => {
        expect(part1(data)).toEqual(68775);
    });
});

describe("check part2", () => {
    it("is correct", () => {
        expect(part2(data)).toEqual(202585);
    });
});
