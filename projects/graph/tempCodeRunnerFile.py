        index = destination_vertex
        linkTo = destination_vertex
        path = []
        path.append(destination_vertex)
        done = False
        while done == False:
            if linkTo in self.vertices[index]:
                path.append(index)
                linkTo = index
                index -= 1
            else:
                index -= 1
            if index < starting_vertex:
                done = True

        path.reverse()
        return path