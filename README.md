# contract-proto

Pure protobuf/gRPC contract registry.

## Layout

| `proto/common/v1/` | envelope, error, pagination |
| `proto/events/v1/` | event contracts |
| `proto/services/v1/` | service contracts |

## Validation

```bash
bash infra/scripts/ci.sh
```

## Rules

- Public contract/asset package only.
- No application data, secrets, or personal data.
- Versioned by tag.
