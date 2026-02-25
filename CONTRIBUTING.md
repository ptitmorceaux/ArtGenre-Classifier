# Contributing Guide

Maintain a clean, linear, and readable Git history using **Rebase and Merge**.

## 1. Branches

Name branches according to the `type/short-description` format (use a `/` after the type):

| Type | Usage |
| --- | --- |
| **feat** | New feature. |
| **fix** | Bug fix. |
| **refactor** | Code modification (neither bug nor feature). |
| **docs** | Documentation (README, comments). |
| **test** | Adding or modifying tests. |
| **chore** | Maintenance, tools, dependencies (e.g., Ruff, Pytest). |

*Example: `refactor/specs-json`*

## 2. Commits (Conventional Commits)

Structure commit messages to clarify scope and action:
`type(scope): description in lowercase without final period`

* `feat(api): add login endpoint`
* `fix(parser): handle empty JSON files`
* `refactor(json): optimize type normalization`

## 3. Pull Requests

Le titre de la PR doit résumer l'objectif global de la branche. Contrairement aux commits, la première lettre est en majuscule.

**Format :** `Type: Description concise`

* `Refactor: Enhance JSON specification logic`
* `Feat: Add OAuth2 authentication`
* `Fix: Resolve memory leak in parser`

## 4. Merge Workflow

1. **Clean history**: Use `git rebase -i` to rename or squash intermediate commits before merging.
2. **Update branch**: Use `git pull --rebase origin main` to integrate the latest changes from `main`.
3. **Update PR**: Use `git push --force-with-lease` after a rebase.
4. **Merge**: Select the **Rebase and merge** option on GitHub.

## 5. Conflict Resolution (Rebase)

In case of conflict during a rebase:

1. Manually resolve conflicts in the affected files.
2. Add the modified files: `git add <file>`.
3. Continue the rebase: `git rebase --continue` (do not create a commit).
4. Cancel in case of error: `git rebase --abort`.
5. **Update PR**: Once the rebase is complete, use `git push --force-with-lease` to synchronize the remote repository.
6. **Merge**: Select the **Rebase and merge** option on GitHub.