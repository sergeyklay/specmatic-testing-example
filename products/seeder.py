# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Seed the database with fake data."""

from faker import Faker
from faker.providers import company, lorem, python

from products.fake import FakeProduct
from .models import db, Product


def seed_products():
    """Add seed product data to the database."""
    db.create_all()

    fake = Faker()

    fake.add_provider(company)
    fake.add_provider(lorem)
    fake.add_provider(python)
    fake.add_provider(FakeProduct)

    for _ in range(1000):
        price = fake.pyfloat(left_digits=3, right_digits=2,
                             min_value=1.0, max_value=999.99)
        product = Product(
            title=' '.join(fake.words(nb=5)).capitalize(),
            description=fake.sentence(nb_words=10),
            price=price,
            discount=fake.pyfloat(left_digits=3, right_digits=2,
                                  min_value=0.0, max_value=price),
            rating=fake.pyfloat(left_digits=1, right_digits=2,
                                min_value=0.0, max_value=5.0),
            stock=fake.pyint(min_value=0, max_value=999),
            brand=fake.company(),
            category=fake.category(),
        )
        product.save()