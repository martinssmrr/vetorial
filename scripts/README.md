# Scripts de Automação

Este diretório contém scripts utilitários para automação de tarefas administrativas.

## 📜 Scripts Disponíveis

### `popular_planos.py`

Popula o banco de dados com planos de exemplo para o sistema de contratação.

**O que faz:**
- Cria 9 planos pré-configurados:
  - 3 planos de Serviços (Bronze, Prata, Ouro)
  - 3 planos de Comércio (Bronze, Prata, Ouro)
  - 2 planos de Abertura de Empresa (ME/EPP, LTDA Premium)
- Define preços, descontos, features e configurações
- Marca planos em destaque
- Define ordem de exibição

**Como executar:**

```bash
# Via Docker (recomendado)
docker-compose exec web python scripts/popular_planos.py

# Via Python diretamente (se não estiver usando Docker)
python scripts/popular_planos.py
```

**Resultado esperado:**
```
🚀 Iniciando população de planos...
✅ 9 planos criados com sucesso!

📊 Resumo:
   - Planos de Serviços: 3
   - Planos de Comércio: 3
   - Planos de Abertura: 3
   - Total: 9

🎯 Planos em Destaque:
   - Prata (Serviços)
   - Prata (Comércio)
   - Abertura ME/EPP (Abertura de Empresa)
```

**Nota:** O script está configurado para **adicionar** planos. Se quiser limpar antes de popular, descomente a linha:
```python
# Plano.objects.all().delete()
```

---

## 🔧 Criando Novos Scripts

Para criar um novo script de automação:

1. Crie um arquivo `.py` neste diretório
2. Adicione o cabeçalho de configuração do Django:

```python
#!/usr/bin/env python
import os
import sys
import django

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vetorial_project.settings')
django.setup()

# Seu código aqui
from apps.services.models import Plano

def meu_script():
    # Lógica do script
    pass

if __name__ == '__main__':
    meu_script()
```

3. Execute com:
```bash
docker-compose exec web python scripts/seu_script.py
```

---

## 📚 Exemplos de Scripts Úteis

### Limpar todos os planos
```python
from apps.services.models import Plano
Plano.objects.all().delete()
print("✅ Todos os planos foram removidos")
```

### Ativar/Desativar planos em lote
```python
from apps.services.models import Plano

# Desativar todos os planos de comércio
Plano.objects.filter(categoria='comercio').update(ativo=False)

# Reativar apenas o plano Prata
Plano.objects.filter(nome='Prata', categoria='comercio').update(ativo=True)
```

### Atualizar preços em massa
```python
from apps.services.models import Plano
from decimal import Decimal

# Aplicar 10% de desconto em todos os planos
for plano in Plano.objects.all():
    plano.preco_antigo = plano.preco
    plano.preco = plano.preco * Decimal('0.9')
    plano.save()
```

### Exportar planos para JSON
```python
import json
from apps.services.models import Plano

planos_data = []
for plano in Plano.objects.all():
    planos_data.append({
        'nome': plano.nome,
        'categoria': plano.categoria,
        'preco': str(plano.preco),
        'features': plano.features,
    })

with open('planos_export.json', 'w', encoding='utf-8') as f:
    json.dump(planos_data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(planos_data)} planos exportados")
```

---

## 🚨 Boas Práticas

1. **Sempre teste em desenvolvimento primeiro**
2. **Faça backup antes de scripts destrutivos**
3. **Use transações para operações críticas**
4. **Adicione logging para debug**
5. **Documente o que o script faz**

---

## 📝 Log de Scripts

| Script | Criado em | Autor | Descrição |
|--------|-----------|-------|-----------|
| popular_planos.py | 21/11/2025 | Sistema | Popula planos iniciais |

---

## 🔗 Links Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Documentação do Projeto](../docs/)
- [Admin de Planos](http://localhost:8000/admin/services/plano/)
