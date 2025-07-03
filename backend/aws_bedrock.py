import json
import boto3

def initialize_bedrock_client(region_name='us-east-1'):
    return boto3.client('bedrock-runtime', region_name=region_name)

def invoke_bedrock_model(client, user_prompt):
    """
    AWS Bedrock modelini çağırır.
    
    Args:
        client: Bedrock runtime boto3 client.
        user_prompt: Modele gönderilecek prompt/metin.
    
    Returns:
        Modelden dönen cevap (JSON veya string).
    """
    system_prompt = """Sen, perakende tekstil sektörü için geliştirilmiş bir ERP yazılımında, admin panelinde görev yapan yapay zeka asistanısın. Nebim ERP sistemine entegresin. Kullanıcıların stok, satış, sipariş, ürün, müşteri ve kasa işlemlerini hızlandırmalarına yardımcı olursun. Her yanıtını Nebim terminolojisi ve veri yapısına göre üretirsin.

Görevlerin:
- Stokları model, beden, renk, sezon bazlı sorgula
- Kritik stoklar için uyar, transfer öner
- Satış/siparişleri özetle, çok satan/zayıf ürünleri analiz et
- İade oranlarını hesapla, öneri ver
- Kasa ve finansal hareketleri raporla
- Müşteri ve bayi performanslarını değerlendir
- KPI ve grafik bazlı karar destek sun
- Kullanıcının yetkisine göre cevap ver, gerektiğinde uyar

Nebim V3 veri yapısına (%100 uyumlu) çalışır, sade, profesyonel ve hızlı yanıtlar verirsin."""

    payload = {
        "prompt": f"{system_prompt}\n\nHuman: {user_prompt}\n\nAssistant:",
        "max_tokens_to_sample": 1500,
        "temperature": 0.7,
        "top_p": 1.0,
        "top_k": 250,
        "stop_sequences": ["\n\nHuman:"]
    }

    response = client.invoke_model(
        modelId='anthropic.claude-instant-v1',
        contentType='application/json',
        accept='*/*',
        body=json.dumps(payload)
    )
    raw_body = response['body'].read()

    response_body = json.loads(raw_body)

    return response_body.get('completion')