import argparse
from .auth import get_service
from .cleaner import clean_emails

def main():
    parser = argparse.ArgumentParser(description='CLI Gmail cleaner')
    parser.add_argument('--sender', nargs='+', help='Sender email(s) to match')
    parser.add_argument('--before', help='Only delete emails before this date (YYYY/MM/DD)')
    parser.add_argument('--after', help='Only delete emails after this date (YYYY/MM/DD)')
    parser.add_argument('--permanent', action='store_true', help='Permanently delete instead of moving to trash')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')

    args = parser.parse_args()

    try:
        # This will also print the authed email
        service, authed_email = get_service(permanent=args.permanent, verbose=args.verbose)
        if args.verbose:
            print(f"[INFO] Using account: {authed_email}")

        clean_emails(
            service,
            sender=args.sender,
            before=args.before,
            after=args.after,
            permanent=args.permanent,
            verbose=args.verbose
        )
    except Exception as e:
        print(f"[FATAL] {e}")
