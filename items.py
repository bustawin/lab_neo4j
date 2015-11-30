from datetime import datetime

line_items = """
    CREATE (
        l1: LineItem {
            orderKey: 1,
            supplierNationKey: 1,
            quantity: 1,
            extendedPrice: 1,
            discount: 1,
            tax: 1,
            returnFlag: "F1",
            lineStatus: "LS1",
            shipDate: """+str(datetime(2015, 1, 2))+""",
        }
    ),
    CREATE (
        l2: LineItem {
            orderKey: 2,
            supplierNationKey: 2,
            quantity: 2,
            extendedPrice: 2,
            discount: 2,
            tax: 2,
            returnFlag: "F2",
            lineStatus: "LS2",
            shipDate: """+str(datetime(2015, 1, 2))+""",
        }
    ),
    CREATE (
        l3: LineItem {
            orderKey: 3,
            supplierNationKey: 3,
            quantity: 3,
            extendedPrice: 3,
            discount: 3,
            tax: 3,
            returnFlag: "F3",
            lineStatus: "LS3",
            shipDate: """+str(datetime(2015, 1, 2))+""",
        }
    )
"""
orders = """
    CREATE (
        o1: Order {
            orderKey: 1,
            shipPriority: "SP1",
            orderDate: """+datetime(2015, 1,1)+"""
        }
    )
    CREATE(
        o2: Order {
            orderKey: 2,
            shipPriority: "SP2",
            orderDate: """+datetime(2015, 1,1)+"""
        }
    )
    CREATE(
        o3: Order {
            orderKey: 3,
            shipPriority: "SP3",
            orderDate: """+datetime(2015, 1,1)+"""
        }
    )
"""
customers = """
    CREATE(
        c1: Customer {
            marketSegment: "MS1",
            nationName: 'n1',
            regionName: 'r1',
        }
    ),
    CREATE(
        c2: Customer {
            marketSegment: "MS3",
            nationName: 'n1',
            regionName: 'r1',
        }
    )
"""
supplier = """
    CREATE(
        s1:{
            name: 'supplier1',
            address: 'address1',
            nationName: 'n1',
            regionName: 'r1',
            phone: '1111',
            accountBalance: 1.0,
            comment: 'comment1'
        }
    )
    CREATE(
        s2:{
            name: 'supplier2',
            address: 'address2',
            nationName: 'n1',
            regionName: 'r1',
            phone: '2222',
            accountBalance: 2.0,
            comment: 'comment2'
        }
    )
    CREATE(
        s3:{
            name: 'supplier3',
            address: 'address3',
            nationName: 'n1',
            regionName: 'r1',
            phone: '3333',
            accountBalance: 3.0,
            comment: 'comment3'
        }
    )
"""
insert_all_query = line_items + orders + customers + supplier
