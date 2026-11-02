/** S5 improved implementation: the lock is checked first and grouping is explicit. */
import type { Doc, User } from "./initial";

export function canEdit(user: User, doc: Doc): boolean {
  if (doc.locked) {
    return false;
  }
  return user.isAdmin || user.id === doc.ownerId;
}
