def dfs(threads: Dict[int, List[Call]], state: State):
        first_op_per_thread = [t.first for t in threads.values()]
        if first_op_per_thread.isEmpty:
            return res
        ref = min(op.end for op first_op_per_thread)
        # candidates are all the operations we can execute next
        # without violating the linearization order
        candidates: List[Call] = [c in first_op_per_thread if c.intersects(ref)]

        for c in candidates:
            try:
                # new execute the operation on a copy of the state
                # and if an execution throws and error, we backtrack
                new_state = c.exec(state.copy())
            except:
                return

            sol = dfs(threads.copy()[c.threadno].popFirst(), new_state)
            res.append(sol)

        return res

      def linearize_generic(spec: List[Call], state: State):
        # sort by thread and then by start time
        threads: Dict[int, List[Call]] = sort_by_thread(spec)
        ret = dfs(threads, state)
      
        return ret
      
          