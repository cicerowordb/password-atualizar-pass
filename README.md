# ATUALIZAR PASS
This component is part of a set of applications according to following diagram:

```
                          ┌───────────┐
                     ┌───►│LISTAR-PASS├────┐
                     │    └───────────┘    │
                     │                     ▼
 ┌────────┐    ┌─────┴──────┐          ┌────────┐
 │INTERNET├───►│GERADOR-PASS├─────────►│DATABASE│
 └────────┘    └─────┬──────┘          └────────┘
                     │                     ▲
                     │   ┌──────────────┐  │
                     └──►│ATUALIZAR-PASS├──┘
                         └──────────────┘
```

Check all necessary information in [GERADOR-PASS REPOSITORY](https://github.com/cicerowordb/password-gerador-pass).


