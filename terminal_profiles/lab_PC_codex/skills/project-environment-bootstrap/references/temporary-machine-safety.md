# Temporary Machine Safety

Use when the user is on a borrowed, temporary or public machine.

## Cautious mode

- Do not record full hostname, username, absolute paths or server addresses unless the user explicitly allows it.
- Do not configure long-lived Git credentials.
- Do not write global git config unless the user explicitly asks.
- Avoid installing global software.
- Prefer temporary or project-local environments.
- Avoid storing notebook tokens or API tokens in files.

## End-of-task reminders

Suggest cleanup when appropriate:

- Remove temporary files.
- Clear shell history if sensitive commands were typed.
- Log out of GitHub or revoke temporary credentials.
- Stop Jupyter servers.
- Delete downloaded sensitive data.
- Remove project copies from public/shared folders.
