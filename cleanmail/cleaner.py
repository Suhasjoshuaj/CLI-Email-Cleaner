def clean_emails(service, sender=None, before=None, after=None, permanent=False, verbose=False):
    from datetime import datetime

    query_parts = []
    if sender:
        if isinstance(sender, list):
            sender_query = " OR ".join([f"from:{s}" for s in sender])
            query_parts.append(f"({sender_query})")
        else:
            query_parts.append(f"from:{sender}")
    if before:
        query_parts.append(f"before:{before}")
    if after:
        query_parts.append(f"after:{after}")

    query = ' '.join(query_parts)

    if verbose:
        print(f"[INFO] Gmail search query: '{query}'")

    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    if not messages:
        print("[INFO] No matching emails found.")
        return

    for msg in messages:
        msg_id = msg['id']
        try:
            if permanent:
                service.users().messages().delete(userId='me', id=msg_id).execute()
            else:
                service.users().messages().trash(userId='me', id=msg_id).execute()
            if verbose:
                print(f"[{'DELETED' if permanent else 'TRASHED'}] {msg_id}")
        except Exception as e:
            print(f"[ERROR] Failed to process {msg_id}: {e}")

    print(f"[DONE] {'Deleted' if permanent else 'Trashed'} {len(messages)} emails.")