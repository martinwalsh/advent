module.exports = {
    root: true,
    parserOptions: {
        tsconfigRootDir: __dirname,
        project: ['./tsconfig.json'],
    },
    overrides: [
        {
            files: ['*.ts'],
            excludedFiles: ['*.test.ts'],
            extends: '@exercism/eslint-config-typescript',
        },
        {
            files: ['*.test.ts'],
            parser: "@babel/eslint-parser",
            plugins: ['jest'],
            extends: ["plugin:jest/recommended"],
            env: {
                "jest/globals": true,
            },
        }
    ],
}
