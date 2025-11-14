import time
import allure
from pages.base_page import BasePage


class DroppablePage(BasePage):
    # simple
    SIMPLE_TAB = '#droppableExample-tab-simple'
    DRAG_ME_SIMPLE = '#draggable'
    DROP_HERE_SIMPLE = '#simpleDropContainer #droppable'

    # accept
    ACCEPT_TAB = '#droppableExample-tab-accept'
    ACCEPTABLE = '#acceptable'
    NOT_ACCEPTABLE = '#notAcceptable'
    DROP_HERE_ACCEPT = '#acceptDropContainer #droppable'

    # prevent Propogation
    PREVENT_TAB = '#droppableExample-tab-preventPropogation'
    NOT_GREEDY_DROP_BOX_TEXT = 'div#notGreedyDropBox p:nth-child(1)'
    NOT_GREEDY_INNER_BOX = '#notGreedyInnerDropBox'
    GREEDY_DROP_BOX_TEXT = 'div#greedyDropBox p:nth-child(1)'
    GREEDY_INNER_BOX = '#greedyDropBoxInner'
    DRAG_ME_PREVENT = '#ppDropContainer #dragBox'

    # revert Draggable
    REVERT_TAB = '#droppableExample-tab-revertable'
    WILL_REVERT = '#revertable'
    NOT_REVERT = '#notRevertable'
    DROP_HERE_REVERT = '#revertableDropContainer #droppable'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/droppable', wait_until='domcontentloaded')

    @allure.step('Drop simple div')
    def drop_simple(self) -> str:
        self.page.locator(self.SIMPLE_TAB).click()
        drag_div = self.page.locator(self.DRAG_ME_SIMPLE)
        drop_div = self.page.locator(self.DROP_HERE_SIMPLE)
        drag_div.drag_to(drop_div)
        return drop_div.inner_text()

    @allure.step('Drop accept div')
    def drop_accept(self, accept: str) -> str:
        accepts = {'acceptable': self.ACCEPTABLE, 'not_acceptable': self.NOT_ACCEPTABLE}
        self.page.locator(self.ACCEPT_TAB).click()
        accept_div = self.page.locator(accepts[accept])
        drop_div = self.page.locator(self.DROP_HERE_ACCEPT)
        accept_div.drag_to(drop_div)
        return drop_div.inner_text()

    @allure.step('Drop prevent propogation div')
    def drop_prevent_propogation(self, propogation: str) -> tuple[str, str]:
        propogations = {'greedy': {'box': self.GREEDY_INNER_BOX, 'text': self.GREEDY_DROP_BOX_TEXT},
                        'not_greedy': {'box': self.NOT_GREEDY_INNER_BOX, 'text': self.NOT_GREEDY_DROP_BOX_TEXT}}
        self.page.locator(self.PREVENT_TAB).click()
        drag_div = self.page.locator(self.DRAG_ME_PREVENT)
        inner_box = self.page.locator(propogations[propogation]['box'])
        drag_div.drag_to(inner_box)
        outer_box_text = self.page.locator(propogations[propogation]['text']).inner_text()
        inner_box_text = inner_box.inner_text()
        return outer_box_text, inner_box_text

    @allure.step('Drag revert draggable div')
    def drop_revert_draggable(self, type_drag: str) -> tuple[str, str]:
        drags = {'will': self.WILL_REVERT, 'not_will': self.NOT_REVERT}
        self.page.locator(self.REVERT_TAB).click()
        revert = self.page.locator(drags[type_drag])
        drop_div = self.page.locator(self.DROP_HERE_REVERT)
        revert.drag_to(drop_div)
        position_after_move = revert.get_attribute('style') or ''
        time.sleep(1)
        position_after_revert = revert.get_attribute('style') or ''
        return position_after_move, position_after_revert
