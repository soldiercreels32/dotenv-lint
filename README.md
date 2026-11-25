# dotenv-lint

Check that every key in `.env.example` exists in `.env`, flag duplicates and report keys that are no longer documented.

## Usage

```bash
python dotenv_lint.py --env .env --example .env.example
```

Exit code is `1` when drift is found, so it can run in CI.
## License

MIT

## Notes

The implementation favors readability over micro-optimizations.
