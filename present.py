def solution(friends, gifts):
    # Initialize data structures
    gift_count = {name: {other: 0 for other in friends} for name in friends}
    given_count = {name: 0 for name in friends}
    received_count = {name: 0 for name in friends}
    
    # Count the gifts given and received
    for record in gifts:
        giver, receiver = record.split()
        gift_count[giver][receiver] += 1
        given_count[giver] += 1
        received_count[receiver] += 1
    
    # Compute gift index for each friend
    gift_index = {name: given_count[name] - received_count[name] for name in friends}
    
    # Calculate gifts to be received next month
    next_month_received = {name: 0 for name in friends}
    n = len(friends)
    for i in range(n):
        for j in range(i + 1, n):
            A = friends[i]
            B = friends[j]
            if gift_count[A][B] > gift_count[B][A]:
                # A gave more gifts to B, so A receives one from B
                next_month_received[A] += 1
            elif gift_count[A][B] < gift_count[B][A]:
                # B gave more gifts to A, so B receives one from A
                next_month_received[B] += 1
            else:
                # Equal gifts exchanged or none; use gift index comparison
                if gift_index[A] > gift_index[B]:
                    next_month_received[A] += 1
                elif gift_index[A] < gift_index[B]:
                    next_month_received[B] += 1
                # if gift_index[A] == gift_index[B], no gift is exchanged
    
    print("Next month received:", next_month_received)
    print("Gift index:", gift_index)
    print("Given count:", given_count)
    print("Received count:", received_count)
    print("Gift count:", gift_count)
    # Return the maximum gifts any friend will receive next month
    return max(next_month_received.values())
