    # -----------------------------------------------------------------
    # Inorder traversal
    # -----------------------------------------------------------------

    def inorder(self) -> Iterator[Tree.Position]:
        """
        Generate positions in inorder.

        Visit the left subtree, then the current position, followed
        by the right subtree.
        """
        root = self.root()

        if root is not None:
            yield from self._subtree_inorder(root)

    def _subtree_inorder(
        self,
        position: Tree.Position
    ) -> Iterator[Tree.Position]:
        """Generate positions in inorder within a binary subtree."""

        left_child = self.left(position)

        if left_child is not None:
            yield from self._subtree_inorder(left_child)

        yield position

        right_child = self.right(position)

        if right_child is not None:
            yield from self._subtree_inorder(right_child)
