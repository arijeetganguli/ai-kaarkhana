package io.kaarkhana.examples.s05;

/** S5 improved implementation: the lock is checked first and grouping is explicit. */
public final class DocumentAccess {
    public record User(long id, boolean admin) {}

    public record Document(long ownerId, boolean locked) {}

    private DocumentAccess() {}

    public static boolean canEdit(User user, Document document) {
        if (document.locked()) {
            return false;
        }
        return user.admin() || user.id() == document.ownerId();
    }
}
