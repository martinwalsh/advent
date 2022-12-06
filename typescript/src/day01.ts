function sum(numbers: Array<number>): number {
    // It seems this form of for-loop is faster than other, nicer syntax.
    // https://stackoverflow.com/questions/1230233/how-to-find-the-sum-of-an-array-of-numbers
    var answer = 0
    for (var i = 0; i < numbers.length; i++) {
        answer += numbers[i]
    }
    return answer
}

function parse(data: string): Array<number> {
    var calories: Array<number> = []
    var elves: Array<string> = data.trim().split("\n\n")
    for (var e = 0; e < elves.length; e++) {
        var elf: Array<string> = elves[e].split("\n")
        calories.push(sum(elf.map((s) => parseInt(s))))
    }
    return calories
}

export function part1(data: string): number {
    return Math.max.apply(null, parse(data))
}

export function part2(data: string): number {
    return sum(parse(data).sort((a, b) => { return a - b }).slice(-3))
}
