#!/usr/bin/env python
"""
Script para popular o banco de dados com planos de exemplo.
Execute com: docker-compose exec web python scripts/popular_planos.py
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vetorial_project.settings')
django.setup()

from apps.services.models import Plano


def popular_planos():
    """Popula o banco com os planos padrão"""
    
    print("🚀 Iniciando população de planos...")
    
    # Limpar planos existentes (opcional - comente se não quiser limpar)
    # Plano.objects.all().delete()
    # print("   Planos anteriores removidos")
    
    planos = []
    
    # ========== PLANOS DE SERVIÇOS ==========
    planos.append(Plano(
        nome="Bronze",
        categoria="servicos",
        preco=259.90,
        preco_antigo=329.90,
        descricao="Perfeito para quem precisa de suporte, autonomia e agilidade no dia a dia.",
        features=[
            "Contabilidade completa",
            "Certificado digital incluído",
            "Painel contábil",
            "Atendimento multicanal (8h-18h)",
            "Painel de RH (até 3 pessoas)",
            "Financeiro automático",
            "Importação até 50 notas fiscais",
            "Link de Pagamento",
            "Benefícios exclusivos"
        ],
        ativo=True,
        destaque=False,
        ordem=1
    ))
    
    planos.append(Plano(
        nome="Prata",
        categoria="servicos",
        preco=349.90,
        preco_antigo=569.90,
        descricao="Tenha um gerente de conta dedicado para sua empresa.",
        features=[
            "Todos os benefícios do Bronze",
            "Gerente de conta exclusivo",
            "Painel de RH (até 5 pessoas)",
            "Importação em qualquer município",
            "IR para sócios",
            "Conciliação financeira",
            "Atendimento estendido (até 21h)",
            "Consultoria contábil",
            "Agendamento/emissão (até 40/mês)",
            "Importação até 100 notas",
            "Importação de extrato (até 2 contas)"
        ],
        ativo=True,
        destaque=True,  # Mais Popular
        ordem=2
    ))
    
    planos.append(Plano(
        nome="Ouro",
        categoria="servicos",
        preco=699.90,
        preco_antigo=879.90,
        descricao="Para quem tem uma operação maior e mais demandas financeiras.",
        features=[
            "Todos os benefícios do Prata",
            "Painel de RH (até 10 pessoas)",
            "Agendamento/emissão (até 100/mês)",
            "Importação até 800 notas",
            "Importação de extrato (até 3 contas)"
        ],
        ativo=True,
        destaque=False,
        ordem=3
    ))
    
    # ========== PLANOS DE COMÉRCIO ==========
    planos.append(Plano(
        nome="Bronze",
        categoria="comercio",
        preco=309.90,
        preco_antigo=379.90,
        descricao="Essencial para quem está começando a vender produtos e precisa de uma contabilidade organizada.",
        features=[
            "Contabilidade completa para comércio",
            "Cálculo de ICMS, PIS/COFINS",
            "Certificado digital incluído",
            "Painel contábil",
            "Atendimento multicanal (8h-18h)",
            "Painel de RH (até 3 pessoas)",
            "Controle de estoque básico",
            "Emissão de até 50 notas (NF-e)",
            "Link de Pagamento",
            "Benefícios exclusivos"
        ],
        ativo=True,
        destaque=False,
        ordem=1
    ))
    
    planos.append(Plano(
        nome="Prata",
        categoria="comercio",
        preco=399.90,
        preco_antigo=619.90,
        descricao="Ideal para lojas em crescimento que buscam mais controle financeiro e fiscal.",
        features=[
            "Todos os benefícios do Bronze",
            "Gerente de conta exclusivo",
            "Painel de RH (até 5 pessoas)",
            "Gestão de impostos (ICMS-ST)",
            "IR para sócios",
            "Conciliação financeira",
            "Atendimento estendido (até 21h)",
            "Emissão de até 150 notas (NF-e)",
            "Importação de extrato (até 2 contas)"
        ],
        ativo=True,
        destaque=True,  # Mais Popular
        ordem=2
    ))
    
    planos.append(Plano(
        nome="Ouro",
        categoria="comercio",
        preco=749.90,
        preco_antigo=929.90,
        descricao="Para operações de e-commerce e varejo com alto volume e maior complexidade.",
        features=[
            "Todos os benefícios do Prata",
            "Painel de RH (até 10 pessoas)",
            "Planejamento tributário",
            "Emissão de até 900 notas (NF-e)",
            "Agendamento de pagamentos (até 100/mês)",
            "Importação de extrato (até 3 contas)"
        ],
        ativo=True,
        destaque=False,
        ordem=3
    ))
    
    # ========== PLANOS DE ABERTURA ==========
    planos.append(Plano(
        nome="Abertura ME/EPP",
        categoria="abertura",
        preco=499.90,
        preco_antigo=799.90,
        descricao="Abertura completa de Microempresa ou EPP com contrato social.",
        features=[
            "Registro na Junta Comercial",
            "Registro no CNPJ",
            "Contrato Social profissional",
            "Alvará de funcionamento",
            "Inscrição Municipal e Estadual",
            "Certificado digital incluso",
            "Suporte especializado",
            "Entrega em até 10 dias úteis"
        ],
        ativo=True,
        destaque=True,  # Mais Popular
        ordem=2
    ))
    
    planos.append(Plano(
        nome="Abertura LTDA Premium",
        categoria="abertura",
        preco=899.90,
        preco_antigo=1299.90,
        descricao="Abertura de LTDA com assessoria jurídica completa e consultoria inicial.",
        features=[
            "Todos os benefícios da ME/EPP",
            "Assessoria jurídica especializada",
            "Consultoria tributária inicial",
            "Registro de marca (opcional)",
            "Planejamento societário",
            "Reunião de kickoff presencial",
            "Gerente dedicado",
            "3 meses de contabilidade grátis",
            "Entrega em até 15 dias úteis"
        ],
        ativo=True,
        destaque=False,
        ordem=3
    ))
    
    # Criar todos os planos
    Plano.objects.bulk_create(planos)
    
    print(f"✅ {len(planos)} planos criados com sucesso!")
    print("\n📊 Resumo:")
    print(f"   - Planos de Serviços: {Plano.objects.filter(categoria='servicos').count()}")
    print(f"   - Planos de Comércio: {Plano.objects.filter(categoria='comercio').count()}")
    print(f"   - Planos de Abertura: {Plano.objects.filter(categoria='abertura').count()}")
    print(f"   - Total: {Plano.objects.count()}")
    
    print("\n🎯 Planos em Destaque:")
    destaques = Plano.objects.filter(destaque=True)
    for plano in destaques:
        print(f"   - {plano.nome} ({plano.get_categoria_display()})")
    
    print("\n💰 Planos com Desconto:")
    com_desconto = Plano.objects.exclude(preco_antigo__isnull=True)
    for plano in com_desconto:
        desconto = plano.percentual_desconto()
        print(f"   - {plano.nome}: {desconto}% OFF (R$ {plano.preco_antigo} → R$ {plano.preco})")
    
    print("\n🌐 Acesse:")
    print("   - Homepage: http://localhost:8000/")
    print("   - Admin: http://localhost:8000/admin/services/plano/")
    print("   - Wizard: http://localhost:8000/services/abertura-empresa/9/")


if __name__ == '__main__':
    try:
        popular_planos()
    except Exception as e:
        print(f"❌ Erro ao popular planos: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
