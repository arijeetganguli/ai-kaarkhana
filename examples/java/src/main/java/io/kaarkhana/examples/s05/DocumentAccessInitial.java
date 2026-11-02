package io.kaarkhana.examples.s05;

/**
 * S5 initial implementation: may a user edit a document?
 *
 * <p>Requirement: a locked document cannot be edited by anyone. Otherwise admins and the owner
 * may edit.
 *
 * <p>PROBLEM: {@code &&} binds tighter than {@code ||}, so this means
 * {@code admin || (owner && !locked)}. Admins bypass the lock.
 */
public final class DocumentAccessInitial {
    private DocumentAccessInitial() {}

    public static boolean canEdit(DocumentAccess.User user, DocumentAccess.Document document) {
        return user.admin() || user.id() == document.ownerId() && !document.locked();
    }
}
