from typing import List

from com.inductiveautomation.ignition.common import BasicDataset
from com.twilio.rest.api.v2010.account import Call
from dev.coatl.helper.types import AnyStr

def getAccounts() -> List[AnyStr]: ...
def getAccountsDataset() -> BasicDataset: ...
def getActiveCalls(accountName: AnyStr) -> List[Call]: ...
def getPhoneNumbers(accountName: AnyStr) -> List[AnyStr]: ...
def getPhoneNumbersDataset(accountName: AnyStr) -> BasicDataset: ...
def sendFreeformWhatsApp(
    accountName: AnyStr, fromNumber: AnyStr, toNumber: AnyStr, message: AnyStr
) -> None: ...
def sendPhoneCall(
    accountName: AnyStr,
    fromNumber: AnyStr,
    toNumber: AnyStr,
    message: AnyStr,
    voice: AnyStr = ...,
    language: AnyStr = ...,
    recordCall: bool = ...,
) -> None: ...
def sendSms(
    accountName: AnyStr, fromNumber: AnyStr, toNumber: AnyStr, message: AnyStr
) -> None: ...
def sendWhatsAppTemplate(
    accountName: AnyStr,
    userNumber: AnyStr,
    whatsAppService: AnyStr,
    whatsAppTemplate: AnyStr,
    templateParameters: AnyStr,
) -> None: ...
