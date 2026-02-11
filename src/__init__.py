from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class Core:
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self._initialized = False
        logger.info(f"Initializing {self.__class__.__name__}")
    
    def initialize(self) -> bool:
        if self._initialized:
            return True
        self._setup()
        self._initialized = True
        return True
    
    def _setup(self) -> None:
        pass
    
    def process(self, data: Any) -> Any:
        if not self._initialized:
            self.initialize()
        return self._handle(data)
    
    def _handle(self, data: Any) -> Any:
        raise NotImplementedError

class Manager:
    def __init__(self):
        self.items: List[Core] = []
    
    def add(self, item: Core) -> None:
        self.items.append(item)
    
    def remove(self, item: Core) -> None:
        self.items.remove(item)
    
    def process_all(self, data: Any) -> List[Any]:
        return [item.process(data) for item in self.items]

__version__ = "1.0.0"
__all__ = ["Core", "Manager"]