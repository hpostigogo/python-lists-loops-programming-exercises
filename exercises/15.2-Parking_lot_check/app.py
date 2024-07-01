parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(list):
  state={'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}
  for i in list:
    for j in i:
      if j == 1:
        state['occupied_slots']+=1
      elif j==2:
        state['available_slots']+=1
  state['total_slots']=state['available_slots']+state['occupied_slots']
  return state

print(get_parking_lot(parking_state))