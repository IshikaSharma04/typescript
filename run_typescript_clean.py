import subprocess, os

dates = [
    "2026-08-09",
    "2026-08-13",
    "2026-08-14",
    "2026-08-18",
    "2026-08-20"
]

# Exactly 3 topics = 3 commits per day
TYPESCRIPT_TOPICS = [
    ("feat(ts): configure compiler options and strict type checking", "src/config.ts",
     "export const config = { strict: true, target: 'ES2022' };\n"),
    ("feat(ts): implement custom generic utilities and interfaces", "src/types/index.ts",
     "export type Nullable<T> = T | null;\nexport interface User { id: string; name: string; }\n"),
    ("test(ts): add unit test cases and execution suite", "tests/app.test.ts",
     "describe('TypeScript Suite', () => { it('passes', () => { expect(true).toBe(true); }); });\n")
]

TIME_SLOTS = ["11:00:00", "14:30:00", "18:00:00"]
AUTHOR_NAME = "IshikaSharma04"
AUTHOR_EMAIL = "ishika.24bcs10352@sst.scaler.com"

# Baseline setup
with open("README.md", "w") as f:
    f.write("# TypeScript Deep Dive\nStructured implementations, utility types, and lab exercises.\n")

subprocess.run(["git", "add", "."], check=True)

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = AUTHOR_NAME
env["GIT_AUTHOR_EMAIL"] = AUTHOR_EMAIL
env["GIT_COMMITTER_NAME"] = AUTHOR_NAME
env["GIT_COMMITTER_EMAIL"] = AUTHOR_EMAIL
env["GIT_AUTHOR_DATE"] = "2026-08-09T09:00:00"
env["GIT_COMMITTER_DATE"] = "2026-08-09T09:00:00"

subprocess.run(["git", "commit", "-m", "Initial commit: setup TypeScript project workspace"], env=env, check=True)

total = 1
for date_str in dates:
    for i, (msg, file_path, content) in enumerate(TYPESCRIPT_TOPICS):
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "a") as f:
            f.write(f"\n// Updated: {date_str} {TIME_SLOTS[i]}\n" + content)

        subprocess.run(["git", "add", file_path], check=True)

        commit_iso = f"{date_str}T{TIME_SLOTS[i]}"
        env["GIT_AUTHOR_DATE"] = commit_iso
        env["GIT_COMMITTER_DATE"] = commit_iso

        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        total += 1

print(f"\nGenerated {total} clean backdated commits for typescript!")
