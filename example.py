import create
import delete
import get
import get_one
import model
import update

df = get.get_db()
print(df)

data = model.data_model(
    date='2022-01-01',
    time='8:00',
    food_item='test2',
    food_cat='test2',
    cal=1000
)
create.put_db(data)

print('get one test :', get_one.get_one_db('637f662bd70b48f9487356cb'))

update.update_db('637f662bd70b48f9487356cb', data)

delete.delete_db('637f662bd70b48f9487356cb')
