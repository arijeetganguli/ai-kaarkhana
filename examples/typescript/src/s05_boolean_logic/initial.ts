/**
 * S5 initial implementation: may a user edit a document?
 *
 * Requirement: a locked document cannot be edited by anyone. Otherwise admins and the
 * owner may edit.
 *
 * PROBLEM: `&&` binds tighter than `||`, so this means `admin || (owner && !locked)`.
 * Admins bypass the lock.
 */
export interface User {
  id: number;
  isAdmin: boolean;
}

export interface Doc {
  ownerId: number;
  locked: boolean;
}

export function canEdit(user: User, doc: Doc): boolean {
  return user.isAdmin || (user.id === doc.ownerId && !doc.locked);
}
