# Signature Verifier

**Signature Verifier** — утилита для проверки подписи сообщения Bitcoin-адресом.

## Как это работает

Bitcoin позволяет подписывать сообщения приватным ключом и проверять их по адресу. Этот инструмент делает проверку офлайн.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python signature_verifier.py <bitcoin_address> <base64_signature> "<original message>"
```

## Пример

```bash
python signature_verifier.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT H0Wxn... "Hello world!"
```

## Зачем

- Подтвердить владение адресом
- Подписать оффчейн-сделки
- Использовать в multisig/DAO/верификациях

## Лицензия

MIT
