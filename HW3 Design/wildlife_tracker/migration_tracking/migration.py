from typing import Any, Optional

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    
    def __init__(self,
                migration_id: int,
                migration_path: MigrationPath,
                current_date: str,
                current_location: str,
                start_date: str,
                duration: Optional[int] = None,
                status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.current_date = current_date
        self.current_location = current_location
        self.start_date = start_date
        self.duration = duration
        self.status = status
    
    def get_migration_details(self) -> dict[str, Any]:
        pass
    
    def update_migration_details(self, **kwargs: Any) -> None:
        pass
    
    def schedule_migration(self,migration_path: MigrationPath) -> None:
        pass
    
    def cancel_migration(self) -> None:
        pass