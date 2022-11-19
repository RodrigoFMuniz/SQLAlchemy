from sqlalchemy import Column, Table, Integer, Numeric, MetaData, ForeignKey

metadata = MetaData()

line_itens = Table(
            'line_itens', 
            metadata,
            Column('line_itens_id', Integer(), primary_key=True),
            Column('order_id', ForeignKey('orders.order_id')),
            Column('cookie_id',ForeignKey('cookies.cookie_id')),
            Column('quantity', Integer()),
            Column('extended_cost', Numeric(12,2))
        )