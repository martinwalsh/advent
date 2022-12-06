module.exports = {
    verbose: true,
    projects: ['<rootDir>'],
    moduleDirectories: ['src', 'node_modules'],
    moduleFileExtensions: ["js", "ts"],
    testMatch: [
        '**/day??.test.ts'
    ],
    testPathIgnorePatterns: [
        '/node_modules/',
        '.d.ts$',
    ],
    transform: {
        '^.+\\.(ts|tsx)?$': 'ts-jest',
    },
}
