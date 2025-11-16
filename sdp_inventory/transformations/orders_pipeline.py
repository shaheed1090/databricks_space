from pyspark import pipelines as dp

@dp.table(name="inventory.orders.bronze_order")
def bronze_order():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/Volumes/inventory/source_data/orders/orders_000.json")
    )